class Product
  attr_reader :name, :weight
  def initialize(name, weight)
    @name = name
    @weight = weight
  end

  def to_s
    "<Product: #{name} (#{weight} lbs)>"
  end
end
