require 'rails_helper'

RSpec.describe BaseDecorator, type: :model do
  describe '.delegate' do
    it 'allows delegation of base object methods' do
      base = double('base')
      BaseDecorator.delegate_methods :spam

      decorator = BaseDecorator.new base
      allow(base).to receive(:spam)
      allow(decorator).to receive(:spam)

      decorator.spam

      expect(base).to have_received(:spam)
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
