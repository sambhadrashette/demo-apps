import {EventEmitter, Injectable} from '@angular/core';
import {Recipe} from './recipe.model';
import {Ingredients} from '../shared/ingredients';
import {ShoppingListService} from '../shopping-list/shopping-list.service';

@Injectable({
  providedIn: 'root'
})
export class RecipeService {
  recipeSelected = new EventEmitter<Recipe>();

  private recipes: Recipe[] = [
    new Recipe('A Test Recipe',
      'A test',
      'https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2015/11/shakshuka-11.jpg',
      [
        new Ingredients('Aa', 1),
        new Ingredients('Bb', 1)
      ]),
    new Recipe('A Test Recipe',
      'A test',
      'https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2015/11/shakshuka-11.jpg',
      [
        new Ingredients('Cc', 1),
        new Ingredients('Dd', 1)
      ]),
  ];

  constructor(private shoppingListService: ShoppingListService) {
  }

  getRecipe() {
    return this.recipes.slice();
  }

  addIngredientsToShoppingList(ingredients: Ingredients[]) {
      this.shoppingListService.addIngredients(ingredients);
  }
}
