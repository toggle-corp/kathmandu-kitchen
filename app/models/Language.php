<?php

class Language extends Model {
    public function get_schema() {
        return [
            ['code', 'string', 'max_length'=>5],
            ['name', 'string', 'max_length'=>255],
        ];
    }
}

?>
