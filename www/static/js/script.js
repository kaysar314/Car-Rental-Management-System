(function() {
  var app;

  app = angular.module('example.app.basic', []);

  app.controller('AppController', [
    '$scope', '$http', function($scope, $http) {
      $scope.posts = [];
      return $http.get('/api/posts').then(function(result) {
        return angular.forEach(result.data, function(item) {
          return $scope.posts.push(item);
        });
      });
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.editor', ['example.api', 'example.app.photos']);

  app.controller('EditController', [
    '$scope', 'Post', function($scope, Post) {
      $scope.newPost = new Post();
      return $scope.save = function() {
        return $scope.newPost.$save().then(function(result) {
          return $scope.posts.push(result);
        }).then(function() {
          return $scope.newPost = new Post();
        }).then(function() {
          return $scope.errors = null;
        }, function(rejection) {
          return $scope.errors = rejection.data;
        });
      };
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.manage', ['example.api', 'example.app.editor']);

  app.controller('DeleteController', [
    '$scope', 'AuthUser', function($scope, AuthUser) {
      $scope.canDelete = function(post) {
        return post.author.username === AuthUser.username;
      };
      return $scope["delete"] = function(post) {
        return post.$delete().then(function() {
          var idx;
          idx = $scope.posts.indexOf(post);
          return $scope.posts.splice(idx, 1);
        });
      };
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.photos', ['example.api']);

  app.controller('AppController', [
    '$scope', 'Post', 'PostPhoto', function($scope, Post, PostPhoto) {
      $scope.photos = {};
      $scope.posts = Post.query();
      return $scope.posts.$promise.then(function(results) {
        return angular.forEach(results, function(post) {
          return $scope.photos[post.id] = PostPhoto.query({
            post_id: post.id
          });
        });
      });
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.playground', ['example.api.playground']);

  app.controller('AppController', [
    '$scope', 'User', function($scope, User) {
      $scope.users = [];
      $scope.newUsername = "";
      $scope.loadUsers = function() {
        return User.query().$promise.then(function(results) {
          return $scope.users = results;
        });
      };
      $scope.addUser = function() {
        var user;
        user = new User({
          username: $scope.newUsername
        });
        $scope.newUsername = "";
        return user.$save().then($scope.loadUsers);
      };
      $scope.deleteUser = function(user) {
        return user.$delete().then($scope.loadUsers);
      };
      return $scope.loadUsers();
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.resource', ['example.api']);

  app.controller('AppController', [
    '$scope', 'Post', function($scope, Post) {
      return $scope.posts = Post.query();
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.static', []);

  app.controller('AppController', [
    '$scope', '$http', function($scope, $http) {
      return $scope.posts = [
        {
          author: {
            username: 'Joe'
          },
          title: 'Sample Post #1',
          body: 'This is the first sample post'
        }, {
          author: {
            username: 'Karen'
          },
          title: 'Sample Post #2',
          body: 'This is another sample post'
        }
      ];
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.update', ['example.api']);

  app.controller('AppController', [
    '$scope', 'User', function($scope, User) {
      $scope.users = [];
      $scope.newUsername = "";
      $scope.loadUsers = function() {
        return User.query().$promise.then(function(results) {
          return $scope.users = results;
        });
      };
      $scope.addUser = function() {
        var user;
        user = new User({
          username: $scope.newUsername
        });
        $scope.newUsername = "";
        return user.$save().then($scope.loadUsers);
      };
      $scope.deleteUser = function(user) {
        return user.$delete().then($scope.loadUsers);
      };
      return $scope.loadUsers();
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.api', ['ngResource']);

  app.factory('User', [
    '$resource', function($resource) {
      return $resource('/api/users/:username', {
        username: '@username'
      });
    }
  ]);

  app.factory('Post', [
    '$resource', function($resource) {
      return $resource('/api/posts/:id', {
        id: '@id'
      });
    }
  ]);

  app.factory('Photo', [
    '$resource', function($resource) {
      return $resource('/api/photos/:id', {
        id: '@id'
      });
    }
  ]);

  app.factory('UserPost', [
    '$resource', function($resource) {
      return $resource('/api/users/:username/posts/:id');
    }
  ]);

  app.factory('PostPhoto', [
    '$resource', function($resource) {
      return $resource('/api/posts/:post_id/photos/:id');
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.api.playground', []);

  app.factory('User', [
    '$q', function($q) {
      var MockUser, i, len, ref, storage, user, username;
      storage = {};
      MockUser = (function() {
        function MockUser(params) {
          var key, value;
          for (key in params) {
            value = params[key];
            this[key] = value;
          }
        }

        MockUser.query = function() {
          var dfr, key, val, values;
          dfr = $q.defer();
          values = (function() {
            var results;
            results = [];
            for (key in storage) {
              val = storage[key];
              results.push(val);
            }
            return results;
          })();
          dfr.resolve(values);
          values.$promise = dfr.promise;
          return values;
        };

        MockUser.save = function(params) {
          var user;
          user = new this(params);
          user.$save();
          return user;
        };

        MockUser.prototype.$save = function() {
          var dfr;
          storage[this.username] = this;
          dfr = $q.defer();
          dfr.resolve(this);
          return dfr.promise;
        };

        MockUser.prototype.$delete = function() {
          var dfr;
          delete storage[this.username];
          dfr = $q.defer();
          dfr.resolve();
          return dfr.promise;
        };

        return MockUser;

      })();
      ref = ['bob', 'sally', 'joe', 'rachel'];
      for (i = 0, len = ref.length; i < len; i++) {
        username = ref[i];
        user = new MockUser({
          username: username
        });
        storage[user.username] = user;
      }
      return MockUser;
    }
  ]);

}).call(this);
