require 'rails_helper'

RSpec.describe ArticleDecorator, type: :model do
  it 'exposes the age of the article in human readable format' do
    decorated = article.decorate

    expect(decorated.age).to eq('Published 1 day ago')
  end
end
