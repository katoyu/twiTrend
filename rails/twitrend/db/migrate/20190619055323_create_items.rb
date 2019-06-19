class CreateItems < ActiveRecord::Migration[5.2]
  def change
    create_table :items do |t|
      t.string :word
      t.integer :count

      t.timestamps
    end
  end
end
