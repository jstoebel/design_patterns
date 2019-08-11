require './box'
require './product'

# b1 = Box.new
# hammer_box = Box.new
# hammer = Product.new 'hammer', 10.0

# hammer_box.add_item hammer
# b1.add_item hammer_box

# recipt = Product.new 'recipt', 0.1
# b1.add_item recipt

# other_box = Box.new

# phone_box = Box.new
# phone = Product.new 'phone', 1.0
# headphones = Product.new 'headpones', 0.1
# phone_box.add_item phone
# phone_box.add_item headphones

# charger_box = Box.new
# charger = Product.new 'charger', 0.1
# charger_box.add_item charger

# other_box.add_item phone_box
# other_box.add_item charger_box

# b1.add_item other_box
# puts b1.instance_variable_get '@contents'
# puts b1.weight

require './shipment'

outer_box = Box.new do
  item Box.new do
    item Product.new 'hammer', 10.0
  end

  # item Product.new 'recipt', 0.1

  # medium_box = Box.new do |mb|
  #   phone_box = Box.new do |pb|
  #     pb.add_item Product.new 'phone', 1
  #     pb.add_item Product.new 'headphones', 0.1
  #   end

  #   charger_box = Box.new do |cb|
  #     cb.add_item Product.new 'charger', 0.1
  #   end

  #   mb.add_item phone_box
  #   mb.add_item charger_box
  # end

  # b.add_item medium_box
end

puts outer_box.weight
