function Movie(name) {
    var self = this;
    self.name = name;
}

function MovieModel(movie){
    var self = this;
    for(var k in movie)
        self[k]=movie[k];
    self.directors = ko.utils.arrayMap(movie.directors, function(director) {
        return new DirectorModel(director);
    });
    self.directors_name = ko.computed(function(){
        str = '';
        for (var i=0; i<self.directors.length; i++){
            if (i) str+= ', ';
            str += self.directors[i].name;
        }
        return str;
    });
    self.full_title = self.title+' ('+self.year+')';

    if (!self.user_data) self.user_data = [];
    //convert all toggle keys to observables
    user_data = ['watched', 'owned', 'liked', 'disliked', 'favorited'];
    for (var key in user_data){
        if (movie.user_data)
            self[user_data[key]] = ko.observable(movie.user_data[user_data[key]]);
        else
            self[user_data[key]] = ko.observable(false);
    }
    console.log(self);
    self.docheckin = function(data, el){
        el.target.innerHTML = 'Checking in ...';
        $.ajax({
                url: '/ajax/movie/checkin/',
                type: 'POST',
                data: {
                    id: self.id
                },

                success: function(message){
                    // upon successful checkin, set watched to true
                    self.watched(true);
                    el.target.innerHTML = 'Checked in!';
                },
                error: function(message){
                    el.target.innerHTML = 'Checked in failed!';
                    alert(message);
                }

            });
    };
}

function DirectorModel(director){
    var self = this;
    for(var k in director) self[k]=director[k];
}

function ListViewModel(data, list_container) {
    if (typeof list_container == 'undefined')
        list_container = 'items';
    var self = this;
    for(var k in data)
        self[k]=data[k];
    self[list_container] = ko.utils.arrayMap(data[list_container], function(item) {
        return new MovieModel(item);
    });
    console.log(self);
}

function MovieViewModel(data) {
    var self = this;
    console.log(data);

    for(var k in data)
        self[k]=data[k];
    // self.items = ko.utils.arrayMap(data.items, function(item) {
    //     return new MovieModel(item);
    // });
    // console.log(self);

}

ko.bindingHandlers.toggle = {
    init: function(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {
        $(element).change(function() {
            //onchange of checkbox update observable
            var value = valueAccessor();
            value(element.checked);
            model_name = viewModel.constructor.name.replace('Model','').toLowerCase();
            className = element.className;
            $(element).addClass('loading');
            $.ajax({
                url: '/ajax/'+model_name+'/',
                type: 'POST',
                data: {
                    id: viewModel.id,
                    attr: className,
                    value: element.checked
                },

                success: function(message){
                    $(element).removeClass('loading');

                },
                error: function(message){
                    $(element).removeClass('loading');
                    //toggle back the checkbox
                    $(element).prop('checked', !$(element).prop('checked'));
                    alert(message);
                }

            });
        });
    },
    update: function(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {
        //on update of observable change checkbox
        var valueUnwrapped = ko.utils.unwrapObservable(valueAccessor());
        element.checked = valueUnwrapped;
    }
};


