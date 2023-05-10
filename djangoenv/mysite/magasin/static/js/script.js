let btns = document.querySelectorAll(".card-body button")

btns.forEach(btn=>{
    btn.addEventListener("click",addtocart)
})

function addtocart(e){
    let product_id = e.target.value
    console.log(product_id)
}