(function( $ ){
	$.fn.headerinteliger = function(options){
		var defaults = {
			img:{
				bannerheader: "/assets/ecommerce_menu/css/BANNER_1460X50_3.png",
				logo: '/assets/ecommerce_menu/css/logo.png',
				iconlogin: '/assets/ecommerce_menu/css/icon-user.png',
				favicon: '/assets/ecommerce_menu/css/icon-heart.png',
				iconcart: '/assets/ecommerce_menu/css/icon-shopping-cart.png',
				linkicon: '/assets/ecommerce_menu/css/torii.png'},
			colorBg:{
				inputcolor: '#fff',
				bgmenu: 'none',
				bgsubmenu: '#ffd200',
			},
			font:{
				fontmenu:{
					fontsize: '11px',
					fontColor: '#315c8e',
					fontfamily: 'Montserrat',
					fontStyle: 'normal'
				},
				fontLogin:{
					fontsize: '12px',
					fontColor: '#315c8e',
					fontfamily: 'Montserrat',
					fontStyle: 'normal'
				},
				fontSubMenu:{
					fontsize: '15px',
					fontColor: '#18537d',
					fontfamily: 'Montserrat',
					fontStyle: 'normal'
				}
			},
			links:{
				menu:[{
					text: 'Coronavírus',
					link:'#'
				},{
					text: 'Dia da Mulher',
					link:'#'
				},{
					text: 'Clube farmacia',
					link:'#'
				},{
					text: 'Clube de vantagens',
					link:'#'
				},{
					text: 'Outlet',
					link:'#'
				}],
				submenu:{
					principal:{
					text:'Todos os departamentos',
						link:'#'
				},
					secundario:[{
					text: 'Cuidado, Proteção e beleza',
					link: '#'
				},{
					text: 'Dermocosméticos',
					link: '#'
				},{
					text: 'Saúde',
					link: '#'
				},{
					text: 'Infantil',
					link: '#'
				},{
					text: 'Conveniência',
					link: '#'
				}]
				}
			},
		};
		var settings = $.extend(true, defaults, options);
		console.log(settings)
		var listaMenu =[];
		settings.links.menu.forEach((value, index) => {
			listaMenu += ''
		});
		var listaSubmenu = [];
		settings.links.submenu.secundario.forEach((value, index) => {
			listaSubmenu += ''
		});
		this.html(`
		`);
		$(".first-block img").attr('src', settings.img.bannerheader);
	}
})( jQuery )

