require './box'
require './product'

class Shipment
  attr_reader :nodes

  def initialize(&block)
    @nodes = []

    @nodes_stack = []

    instance_eval(&block)

    freeze
  end

  def box
    parent = @nodes_stack.empty? ? Box::ROOT : @nodes_stack.alst
  end
end
