require 'delegate'

class BaseDecorator
  attr_reader :object

  # dynamically assign what methods are delegated from the base object
  def self.delegate_methods(*methods)
    methods.each { |method| delegate method, to: :object }
  end

  def initialize(base_object)
    @object = base_object
  end
end
