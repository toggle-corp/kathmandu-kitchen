<?php

require_once 'app/core/Form.php';
require_once 'app/models/Category.php';
require_once 'app/models/FoodItem.php';
require_once 'app/models/FoodTag.php';

require_once 'app/forms/LocalesForm.php';


class FoodTagForm extends Form {
    public function get_schema() {
        return [
            ['value', 'child', 'form'=>'LocalesForm'],
        ];
    }

    public static function get_model_class() {
        return 'FoodTag';
    }
}


class CategoryForm extends Form {
    public function get_schema() {
        return [
            ['name', 'child', 'form'=>'LocalesForm'],
            ['image', 'file', 'dir'=>'uploads', 'max_length'=>255],
        ];
    }

    public static function get_model_class() {
        return 'Category';
    }
}


class FoodItemForm extends Form {
    public function get_schema() {
        return [
            ['category', 'foreign', 'model'=>'Category'],
            ['name', 'child', 'form'=>'LocalesForm'],
            ['image', 'file', 'dir'=>'uploads', 'max_length'=>255],
            ['price', 'float'],
            ['description', 'child', 'form'=>'LocalesForm'],
            ['tags', 'children', 'singular'=>'tag', 'form'=>'FoodTagForm'],
        ];
    }

    public static function get_model_class() {
        return 'FoodItem';
    }
}

?>
