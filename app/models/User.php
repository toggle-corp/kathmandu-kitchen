<?php

class User extends Model {
    public function get_schema() {
        return [
            ["username", "string", "unique"=>true],
            ["password", "string", "max_length"=>255],
        ];
    }
}

 ?>
