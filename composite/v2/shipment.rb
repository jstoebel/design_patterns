require './v2/box'
require './v2/product'

class Shipment
  def initialize(&block)
    @nodes_stack = []
    @root_box = Box.new
    instance_eval(&block)
    freeze
  end

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

  # how many products in this shipment?
  def item_count
    @root_box.item_count
  end

  def weight
    @root_box.weight
  end

  private

  # ads a node to the shipment tree.
  # node: a node like object (Box or Product)
  def add_node(node, &block)
    # apppend node to list of nodes
    # if no block given return
    # push node to the stack
    # eval node's block
    #   -> this will lead to some recursion
    # when we resurface (all children have been delt with), pop node from the stack

    return unless block_given?

    @nodes_stack << node
    instance_eval(&block)
    @nodes_stack.pop
  end

  # returns the parent of the node being created.
  # this is defined as the top node on the stack. 
  # If stack is empty, it means its a top level item of the shipment.
  # push it to the @root_box
  def parent
    @nodes_stack.empty? ? @root_box : @nodes_stack.last
  end
end
