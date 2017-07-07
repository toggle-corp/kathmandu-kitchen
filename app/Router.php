<?php

class Router extends RouterBase
{
    public function __construct()
    {
        $this->routing_rules = array(
            '^$' => ['template', 'home.html'],

            '^admin$' => ['controller', 'AdminController'],

            '^admin/language' =>['controller', 'AdminController:language'],
            '^admin/language/(?<language_id>\d+)' =>['controller', 'AdminController:language'],

            '^admin/category' =>['controller', 'AdminController:category'],
            '^admin/category/(?<category_id>\d+)' =>['controller', 'AdminController:category'],

            '^admin/food-item' =>['controller', 'AdminController:food_item'],
            '^admin/food-item/(?<food_item_id>\d+)' =>['controller', 'AdminController:food_item'],
        );
    }
}

?>
