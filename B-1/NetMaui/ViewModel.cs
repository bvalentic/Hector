public class MainViewModel : INotifyPropertyChanged
{
    private readonly IProductService _productService;

    public MainViewModel(IProductService productService)
    {
        _productService = productService;
        LoadProductsCommand = new Command(async () => await LoadProducts());
    }

    public ObservableCollection<Product> Products { get; } = new ObservableCollection<Product>();

    public ICommand LoadProductsCommand { get; }

    private async Task LoadProducts()
    {
        var products = await _productService.GetProductsAsync();
        foreach (var product in products)
        {
            Products.Add(product);
        }
    }

    public event PropertyChangedEventHandler PropertyChanged;

    protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
