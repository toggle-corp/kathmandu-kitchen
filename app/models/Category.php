<?php

class Category extends Model {
    public function get_schema() {
        return [
            ['name', 'integer'],
            ['image', 'string', 'max_length'=>255, 'null'=>true],
        ];
    }
}

?>
