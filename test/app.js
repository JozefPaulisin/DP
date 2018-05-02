var express     = require("express"),
    app         = express(),
    bodyParser  = require("body-parser"),
    formOutput  =[];


app.use(bodyParser.urlencoded({extended: true}));
app.set('view engine', 'ejs');

app.use(express.static(__dirname + '/public'));


//ROUTES
app.get('/', function(req, res){
    res.render('landing');
});

app.get('/dashboard', function(req, res){
    res.render('dashboard');
});

app.get('/dashboard', function(req, res){
    res.render('dashboard');
});

app.get('/about', function(req, res) {
    res.render('partials/about');
});

app.get('/october', function(req, res) {
    res.render('partials/october');
});

app.get('/november', function(req, res) {
    res.render('partials/november');
});

app.get('/december', function(req, res) {
    res.render('partials/december');
});



app.listen(process.env.PORT, process.env.HOST, function(){
    console.log('Aplikacia funguje!');
});
