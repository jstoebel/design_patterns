class Product
  attr_reader :name, :weight, :item_count
  def initialize(name, weight)
    @name = name
    @weight = weight
    @item_count = 1
  end

  def to_s
    "<Product: #{name} (#{weight} lbs)>"
  end
end