const products = [
    {
      name: "Product 1",
      price: "499 บาท",
      image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/large/6e11ccf3eee48b1369f039632f17fa054494df9f_xxl-1.jpg"
    },
    {
        name: "Product 2",
        price: "599 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/large/2dd35db6a97f21cadb7f6e8770509155e5a219e5_xxl-1.jpg"
      },
      {
        name: "Product 3",
        price: "699 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/large/2f68350a9dbd5b83dc1c8a3763a88fdbf1a95383_xxl-1.jpg"
      },
      {
        name: "Product 4",
        price: "299 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/large/d6cf9c07b219a457b1d19c5790d91e2cc7a3997f_xxl-1.jpg"
      },
      {
        name: "Product 5",
        price: "1,599 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/b80ab47e92c1701b2e49852e1dff7dcb52c492bc_xxl-1.jpg"
      },
      {
        name: "Product 6",
        price: "2,499 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/4096c308a5197078414b011297492fce1e116ff4_xxl-1.jpg"
      },
      {
        name: "Product 7",
        price: "3,249 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/9e4ff8a92716f5130d2a45dd1e99f3485b8a9669_xxl-1.jpg"
      },
      {
        name: "Product 8",
        price: "1,899 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/fa17a938bf52de3a19e53a24c9405e6a9c4ee6c7_xxl-1.jpg"
      },
      {
        name: "Product 9",
        price: "3,999 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/da13f1f94371e05bf2295444cba353a58213b2ab_xxl-1.jpg"
      },
      {
        name: "Product 10",
        price: "1,499 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/2c4724211d8f6d6f23adf6ad0e61ffc3a041f0bb_xxl-1.jpg"
      },
      {
        name: "Product 11",
        price: "2,399 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/6be4290c85f04683ae275486493865521d05be73_xxl-1.jpg"
      },
      {
        name: "Product 12",
        price: "2,799 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/dbf52b53ccd3fe219b61655b5855c4c8c7e527b8_xxl-1.jpg"
      },
      {
        name: "Product 13",
        price: "4,999 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/53940806044884e8440ea7e00d5dfc3e96e10afa_xxl-1.jpg"
      },
      {
        name: "Product 14",
        price: "4,999 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/53940806044884e8440ea7e00d5dfc3e96e10afa_xxl-1.jpg"
      },
      {
        name: "Product 15",
        price: "4,999 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/53940806044884e8440ea7e00d5dfc3e96e10afa_xxl-1.jpg"
      },
      {
        name: "Product 16",
        price: "4,999 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/53940806044884e8440ea7e00d5dfc3e96e10afa_xxl-1.jpg"
      },
      {
        name: "Product 16",
        price: "4,999 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/53940806044884e8440ea7e00d5dfc3e96e10afa_xxl-1.jpg"
      },
      {
        name: "Product 16",
        price: "4,999 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/53940806044884e8440ea7e00d5dfc3e96e10afa_xxl-1.jpg"
      },
      {
        name: "Product 16",
        price: "4,999 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/53940806044884e8440ea7e00d5dfc3e96e10afa_xxl-1.jpg"
      },
      {
        name: "Product 16",
        price: "4,999 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/53940806044884e8440ea7e00d5dfc3e96e10afa_xxl-1.jpg"
      },
      {
        name: "Product 16",
        price: "4,999 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/medium/53940806044884e8440ea7e00d5dfc3e96e10afa_xxl-1.jpg"
      }
  ];
  
  function createProductCard(product) {
    const card = document.createElement("div");
    card.classList.add("card-box");
  
    const image = document.createElement("img");
    image.src = product.image;
    image.classList.add("card-img");
  
    const cardContent = document.createElement("div");
    cardContent.classList.add("card-content");
  
    const cardTitle = document.createElement("h3");
    cardTitle.classList.add("card-title");
    cardTitle.textContent = product.name;
  
    const cardText = document.createElement("p");
    cardText.classList.add("card-text");
    cardText.textContent = product.price;
  
    cardContent.appendChild(cardTitle);
    cardContent.appendChild(cardText);
  
    card.appendChild(image);
    card.appendChild(cardContent);
  
    return card;
  }
  
  function appendProductsToContainer(products) {
    const productContainer = document.getElementById("productContainer");
  
    products.forEach((product) => {
      const card = createProductCard(product);
      productContainer.appendChild(card);
    });
  }
  appendProductsToContainer(products);