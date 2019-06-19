class ShowController < ApplicationController
  def go
    a = Item.all
    @data = a.sample
  end
end
