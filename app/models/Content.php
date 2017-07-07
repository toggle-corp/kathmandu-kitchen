<?php

class Content extends Model {
    public function get_schema() {
        return [
            ['tag', 'string', 'max_length'=>255],
            ['value', 'integer'],
        ];
    }
}

?>
