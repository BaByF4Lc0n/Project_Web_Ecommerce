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
        price: "799 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/large/2f68350a9dbd5b83dc1c8a3763a88fdbf1a95383_xxl-1.jpg"
      },
      {
        name: "Product 5",
        price: "799 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/large/2f68350a9dbd5b83dc1c8a3763a88fdbf1a95383_xxl-1.jpg"
      },
      {
        name: "Product 6",
        price: "799 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/large/2f68350a9dbd5b83dc1c8a3763a88fdbf1a95383_xxl-1.jpg"
      },
      {
        name: "Product 7",
        price: "799 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/large/2f68350a9dbd5b83dc1c8a3763a88fdbf1a95383_xxl-1.jpg"
      },
      {
        name: "Product 8",
        price: "799 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/large/2f68350a9dbd5b83dc1c8a3763a88fdbf1a95383_xxl-1.jpg"
      },
      {
        name: "Product 9",
        price: "799 บาท",
        image: "https://d29c1z66frfv6c.cloudfront.net/pub/media/catalog/product/large/2f68350a9dbd5b83dc1c8a3763a88fdbf1a95383_xxl-1.jpg"
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