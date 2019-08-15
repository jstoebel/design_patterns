class Box
  attr_reader :contents

  def initialize
    @contents = []
  end

  # load an item into this box
  # item: either a Box or a Product
  def pack(item)
    @contents << item
  end

  def weight
    @contents.inject(0.0) { |total, item| total + item.weight }
  end

  def item_count
    @contents.inject(0) { |total, item| total + item.item_count }
  end

  def to_s
    "<Box:#{object_id} #{@contents.length} item(s) (#{weight} lbs) >"
  end
end

