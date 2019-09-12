require 'rails_helper'

RSpec.describe ApplicationRecord, type: :model do

  class TestDecorator; end
  describe '#decorate' do
    it 'returns a decorated object based on convention' do
      model_instance = ApplicationRecord.new
      
      expect(Test)
    end
  end
end
