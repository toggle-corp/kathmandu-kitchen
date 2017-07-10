<?php

class FoodItem extends Model {
    public function get_schema() {
        return [
            ['category', 'integer'],
            ['default_name', 'string', 'max_length'=>255],
            ['name', 'integer', 'delete'=>'locales'],
            ['image', 'string', 'max_length'=>255, 'null'=>true],
            ['price', 'float', 'decimal'=>2],
            ['description', 'integer', 'delete'=>'locales'],
        ];
    }
}

?>
