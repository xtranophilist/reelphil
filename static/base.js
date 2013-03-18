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
    if (!self.user_data) self.user_data = [];

    //convert all toggle keys to observables
    user_data = ['watched', 'owned', 'liked', 'disliked', 'favorited'];
    for (var key in user_data){
        if (movie.user_data)
            self[user_data[key]] = ko.observable(movie.user_data[user_data[key]]);
        else
            self[user_data[key]] = ko.observable(false);
    }
}

function DirectorModel(director){
    var self = this;
    for(var k in director) self[k]=director[k];
}

function ListViewModel(data) {
    var self = this;
    for(var k in data)
        self[k]=data[k];
    self.items = ko.utils.arrayMap(data.items, function(item) {
        return new MovieModel(item);
    });
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
                    // alert(message);

                },
                error: function(message){
                    $(element).removeClass('loading');
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


