class ArticleDecorator < BaseDecorator
  # returns a humanized string describing how long ago the article was published
  delegate_methods :published_at
  include ActionView::Helpers::DateHelper
  def age
    "Published #{time_ago_in_words(published_at)} ago"
  end
end
