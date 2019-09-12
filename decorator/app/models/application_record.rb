class ApplicationRecord < ActiveRecord::Base
  self.abstract_class = true

  def decorate
    "#{self.class}Decorator".constantize.new(self)
  end
end