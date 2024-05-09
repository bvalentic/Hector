public interface IProductService
{
    Task<List<Product>> GetProductsAsync();
}
