class ArticleDecorator < BaseDecorator
  # returns a humanized string describing how long ago the article was published
  delegate_methods :title
  include ActionView::Helpers::DateHelper
  def age
    "Published #{time_ago_in_words(object.published_at)} ago"
  end
end
