class ShowController < ApplicationController
  def go
    @items = Item.select('word, count, created_at').order(created_at: :desc).order(count: :desc).group(:word, :count, :created_at)
  end
end
