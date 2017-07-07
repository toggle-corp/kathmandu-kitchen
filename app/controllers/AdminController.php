<?php

require_once 'app/core/session/Auth.php';
require_once 'app/models/User.php';
require_once 'app/forms/LocalesForm.php';
require_once 'app/forms/MenuForm.php';


class AdminController extends Controller {
    public function get() {
        $user = Auth::get_user('User');
        if ($user) {
            return $this->get_admin_panel();
        }

        $data = [];
        $data['new_user'] = !User::query()->first();
        return new TemplateView('admin/login.html', $data);
    }

    public function get_admin_panel() {
        $data = [];

        $models = [];
        
        $model = [];
        $model['title'] = 'Language';
        $model['id'] = 'languages';
        $model['url'] = 'admin/language';
        $model['items'] = Language::query()->get();
        $models[] = $model;
        
        $model = [];
        $model['title'] = 'Category';
        $model['id'] = 'categories';
        $model['url'] = 'admin/category';
        $model['items'] = Category::query()->get();
        $models[] = $model;
        
        $model = [];
        $model['title'] = 'FoodItem';
        $model['id'] = 'food_items';
        $model['url'] = 'admin/food-items';
        $model['items'] = FoodItem::query()->get();
        $models[] = $model;

        $data['models'] = $models;
        return new TemplateView('admin/admin.html', $data);
    }

    public function post() {
        $data = [];

        if (isset($_POST['register'])) {
            if ($_POST['password'] != $_POST['retype_password']) {
                $data['error'] = 'Passwords do not match';
            }
            else {
                $username = $_POST['username'];
                $password = $_POST['password'];

                $user = new User();
                $user->username = $username;
                Auth::set_password($user, $password);
                $user->save();
            }
        }
        else {
            $username = $_POST['username'];
            $password = $_POST['password'];

            $user = User::query()->where("username=?", $username)->first();
            if ($user && Auth::authenticate($user, $password)) {
                redirect('admin');
            }
            else {
                $data['error'] = 'Invalid username and/or password';
            }
        }

        $data['new_user'] = !User::query()->first();
        return new TemplateView('admin/login.html', $data);
    }

    public function get_admin($form, $id, $model_class, $admin_path, $title) {
        $user = Auth::get_user('User');
        if (!$user) {
            redirect('admin');
        }

        $data = [];
        $data['form'] = $form;
        $data['title'] = $title;

        if ($id != null) {
            $obj = $model_class::query()->where('id=?', $id)->first();
            if (!$obj) {
                redirect("admin/$admin_path");
            }
            $data['obj'] = $obj;
            $data['form']->set_object($obj);
        }

        return new TemplateView('admin/admin.html', $data);
    }

    public function post_admin($form, $id, $model_class, $admin_path, $title) {
        $user = Auth::get_user('User');
        if (!$user) {
            redirect('admin');
        }


        if ($id != null) {
            $obj = $model_class::query()->where('id=?', $id)->first();
            if ($_POST['delete']) {
                $obj->delete();
                redirect('admin#' . strtolower($title));
            }

            $form->set_object($obj);
        }
        $obj = $form->post();
        $id = $obj->id;

        redirect('admin#' . strtolower($title));
    }

    public function get_language($language_id=null) {
        return $this->get_admin(new LanguageForm(), $language_id, 'Language', 'language', 'Languages');
    }

    public function post_language($language_id=null) {
        return $this->post_admin(new LanguageForm(), $language_id, 'Language', 'language', 'Languages');
    }

    public function get_category($category_id=null) {
        return $this->get_admin(new CategoryForm(), $category_id, 'Category', 'category', 'Categories');
    }

    public function post_category($category_id=null) {
        return $this->post_admin(new CategoryForm(), $category_id, 'Category', 'category', 'Categories');
    }

    public function get_food_item($food_item_id=null) {
        return $this->get_admin(new FoodItemForm(), $food_item_id, 'FoodItem', 'food_item', 'Food Items');
    }

    public function post_food_item($food_item_id=null) {
        return $this->post_admin(new FoodItemForm(), $food_item_id, 'FoodItem', 'food_item', 'Food Items');
    }


}

?>
