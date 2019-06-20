class ShowController < ApplicationController
  def go
    @items = Item.select('word, count').order(count: :desc).group(:word, :count)
  end
end
