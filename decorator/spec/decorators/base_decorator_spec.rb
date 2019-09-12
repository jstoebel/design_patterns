require 'rails_helper'

RSpec.describe BaseDecorator, type: :model do
  describe '.delegate' do
    it 'allows delegation of base object methods' do
      base = double('base', spam: 'hello from spam')
      BaseDecorator.delegate_methods :spam

      decorator = BaseDecorator.new base

      expect(decorator.spam).to eq('hello from spam')
    end
  end

  describe '#initialize' do
    it 'exposes the base_object' do
      base = double('base')
      decorator = BaseDecorator.new(base)
      expect(decorator.object).to eq(base)
    end
  end
end
