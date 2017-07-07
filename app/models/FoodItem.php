<?php

class FoodItem extends Model {
    public function get_schema() {
        return [
            ['category', 'integer'],
            ['name', 'integer'],
            ['image', 'string', 'max_length'=>255, 'null'=>true],
            ['price', 'float', 'decimal'=>2],
            ['description', 'integer'],
        ];
    }
}

?>
