problem borrowed from [here](https://refactoring.guru/design-patterns/composite)

Let's say that I am building inventory tracking software for a company that has to package and ship complex orders of products. An order is a box. A box can contain other boxes or products. I need a way to get the total weight of any given box. The composite pattern let's me strucutre all of this as a tree. Both the `Box` and `Product` type respond to the `weight` method. Products know their own weight. Boxes ask all of their direct children their weight and return the sum.

```
require './box'
require './product'

b1 = Box.new
hammer_box = Box.new
hammer = Product.new 'hammer', 10.0

hammer_box.add_item hammer
b1.add_item hammer_box

recipt = Product.new 'recipt', 0.1
b1.add_item recipt

other_box = Box.new

phone_box = Box.new
phone = Product.new 'phone', 1.0
headphones = Product.new 'headpones', 0.1
phone_box.add_item phone
phone_box.add_item headphones

charger_box = Box.new
charger = Product.new 'charger', 0.1
charger_box.add_item charger

other_box.add_item phone_box
other_box.add_item charger_box

b1.add_item other_box
puts b1.instance_variable_get '@contents'
puts b1.weight
```

This is convenient because we have a common interface for getting at item (either product or collection of products) weight. Think of it another way, if I want to know the weight of an item, I shouldn't have to be concerned with dumping out its entire contents and computing it myself. Instead just pass the `weight` message and let my objects do their thing.