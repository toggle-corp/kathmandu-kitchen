<?php

require_once 'app/core/Form.php';
require_once 'app/models/Language.php';
require_once 'app/models/LocaleString.php';
require_once 'app/models/Locales.php';


class LanguageForm extends Form {
    public function get_schema() {
        return [
            ['code', 'string', 'max_length'=>5],
            ['name', 'string', 'max_length'=>255],
        ];
    }

    public static function get_model_class() {
        return 'Language';
    }
}


class LocaleStringForm extends Form {
    public function get_schema() {
        return [
            ['language', 'foreign', 'model'=>'Language', 'name_field'=>'name'],
            ['value', 'text'],
        ];
    }

    public static function get_model_class() {
        return 'LocaleString';
    }
}


class LocalesForm extends Form {
    public function get_schema() {
        return [
            ['strings', 'children', 'singular'=>'string', 'form'=>'LocaleStringForm'],
        ];
    }

    public static function get_model_class() {
        return 'Locales';
    }
}

?>
