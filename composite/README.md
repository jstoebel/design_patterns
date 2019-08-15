Problem borrowed from [here](https://refactoring.guru/design-patterns/composite)

Let's say that I am building inventory tracking software for a company that has to package and ship complex orders of products. An order is a box. A box can contain other boxes or products. I need a way to get the total weight and inventory count of any given box. The composite pattern let's me strucutre all of this as a tree. Both the `Box` and `Product` type respond to the `weight` and `item_count` method. Products know their own weight and that they have an item count of 1 (duh). Boxes ask all of their direct children their weight and item_count and return the sum. Recursion!

```
require './v1/box'
require './v1/product'

b1 = Box.new
hammer_box = Box.new
hammer = Product.new 'hammer', 10.0

hammer_box.add_item hammer
b1.add_item hammer_box

recipt = Product.new 'recipt', 0
b1.add_item recipt

other_box = Box.new

phone_box = Box.new
phone = Product.new 'phone', 1.0
headphones = Product.new 'headpones', 0.1
phone_box.add_item phone
phone_box.add_item headphones

charger_box = Box.new
charger = Product.new 'charger', 0.2
charger_box.add_item charger

other_box.add_item phone_box
other_box.add_item charger_box

b1.add_item other_box

puts "shipment: #{b1.item_count} item(s), #{b1.weight} lbs"
```

This is convenient because we have a common interface for getting at item's (either product or collection of products) weight and count. Think of it another way, if I want to know the weight of an item, I shouldn't have to be concerned with dumping out its entire contents and computing it myself. Instead just pass the `weight` message and let my objects do their thing.

The above code gets the job done, but its awfully verbose. Defining a product on one line and then telling it what box it goes in is tedious. Instead lets use the builder pattern and blocks to specify how we want things structured.

```
require './v2/shipment'

s = Shipment.new do
  box do
    product 'hammer', 10.0
  end

  box do
    box do
      product 'phone', 1.0
      product 'headphones', 0.1
    end

    box do
      product 'charger', 0.2
    end
  end

  product 'recipt', 0
end

puts "shipment: #{s.item_count} item(s), #{s.weight} lbs"
```

Ah, much better! Now we have a `Shipment` instance which represents all of the items in a shipment. `Shipment` has two public methods `box` and `product` to let us define those items

```
  def box(&block)
    box = Box.new
    parent.pack box
    add_node(box, &block)
  end

  def product(name, weight)
    product = Product.new(name, weight)
    parent.pack product
    add_node(product)
  end
```

Both of those methods use a method called `add_node` to add keep track of the item

```
  # ads a node to the shipment tree.
  # node: a node like object (Box or Product)
  def add_node(node, &block)
    # apppend node to list of nodes
    # if no block given return
    # push node to the stack
    # eval node's block
    #   -> this will lead to some recursion
    # when we resurface (all children have been delt with), pop node from the stack

    @nodes << node

    return unless block_given?

    @nodes_stack << node
    instance_eval(&block)
    @nodes_stack.pop
  end
```

Basically we are recursively evaling blocks until we get to a leaf node (product). It uses a stack to keep track of previous items added. At any given time when we are adding an item, its parent is the last item on the stack. If the stack is empty the item's parent is the top level box (stored as `@root_box`). Shipment handles creating an item, adding it to the stack and loading it into its parent box. The win here is that we've now created an interface that lets us simply express the structure of a shipment, and not worry about the messy details of loading products and boxes in to their parent.