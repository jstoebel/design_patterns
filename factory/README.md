The Factory Pattern provides a way for a client to instantiate different object without having to know which classes they need. The objective is to provide a simple interface that doesn't need to change when new classes are added or removed.

To take a trivial example, let's say I am building an app for a university. I have two classes `Student` and `Faculty` who share a common interface.
```ruby
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
```

Let's also say that, for reasons that escape us, we don't want to make a single interface for creating instances of both classes:

```ruby
class PersonFactory
  def self.for(type, attrs)
    Object.const_get(type).new attrs
  end
end
```

Now the details of which object should be returned are hidden from the client. The client provides some data and get's back the appropriate class. This is helpful as when things get more complicated, we don't need to burden client code with logic to decide what subclass to create. The factory decides for you.

