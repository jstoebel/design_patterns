class Box
  attr_reader :contents

  ROOT = Box.new()
  def initialize(parent)
    @parent.parent
  end

  def item(item)
    puts "adding item #{item}"
    @contents << item
  end

  def weight
    @contents.inject(0.0) { |total, item| total + item.weight }
  end

  # recursivly prints a box's complete contents
  def full_inventory
  
  end

  def to_s
    "<Box:#{object_id} #{@contents.length} item(s) weight: #{weight} >"
  end
end
