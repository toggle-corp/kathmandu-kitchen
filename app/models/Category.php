<?php

class Category extends Model {
    public function get_schema() {
        return [
            ['default_name', 'string', 'max_length'=>255],
            ['name', 'integer'],
            ['image', 'string', 'max_length'=>255, 'null'=>true],
        ];
    }
}

?>
