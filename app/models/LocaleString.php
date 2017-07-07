<?php

class LocaleString extends Model {
    public function get_schema() {
        return [
            ['locales', 'integer', 'null'=>true],
            ['language', 'integer'],
            ['value', 'text'],
        ];
    }
}

?>
