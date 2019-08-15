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