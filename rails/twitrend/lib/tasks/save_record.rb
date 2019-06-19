class SaveRecord
  def save
   tree = Tree.new
   tree.name = "maple"
   tree.save
  end
 end
 
 t = SaveRecord.new
 t.save
 p "done"
 