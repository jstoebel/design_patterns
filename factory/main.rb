class Person
  def initialize(attrs)
    @name = attrs[:name]
  end
end

class Student < Person
  def initialize(attrs)
    super
    @grad_class = attrs[:grad_class]
  end

  def to_s
    "#{@name} (#{@grad_class})"
  end
end

class Faculty < Person
  def initialize(attrs)
    super
    @department = attrs[:department]
  end

  def to_s
    "#{@name}, Professor of #{@department}"
  end
end

class PersonFactory
  def self.for(type, attrs)
    Object.const_get(type).new attrs
  end
end

student = PersonFactory.for 'Student', name: 'A Student', grad_class: 2020
puts student

prof = PersonFactory.for 'Faculty', name: 'Dr. Professor Science', department: 'Rocket Surgery'
puts prof
