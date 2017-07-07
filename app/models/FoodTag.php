<?php

class FoodTag extends Model {
    public function get_schema() {
        return [
            ['food_item', 'integer'],
            ['value', 'integer'],
        ];
    }
}

?>
