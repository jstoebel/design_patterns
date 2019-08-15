class Box
  attr_reader :contents

  def initialize
    @contents = []
  end

  def add_item(item)
    @contents << item
  end

  def weight
    @contents.inject(0.0) { |total, item| total + item.weight }
  end

  def item_count
    @contents.inject(0) { |total, item| total + item.item_count }
  end
  def to_s
    "<Box:#{object_id} #{@contents.length} item(s) weight: #{weight} >"
  end
end
