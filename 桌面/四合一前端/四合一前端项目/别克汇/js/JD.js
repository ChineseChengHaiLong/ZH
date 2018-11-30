$(function(){
	// 操作下拉菜单6个
	showhide();
	// 操作二级菜单
	hoverSubMenu();
	//获取焦点。失去焦点。抬起键盘三个事件
	//搜索
	seach();
	// 显示qq空间
	share();
	// 鼠标移入移出显示与隐藏
	address();
	// 点击切换地址
	clickTabs();
	// 鼠标移入移出切换 mini购物车
	hoverminicart();

	// 点击切换产品选项（商品详情等显示出来）
	clickProductTabs();
	// 商品图移动
	moveMiniImg();
	//当鼠标悬停在摸个小图上，在上方显示对应的中图
	hoverMiniImg();

	bigImg();
	function bigImg(){
		var $mediumImg = $('#mediumImg');//中图
		var $mask = $('#mask');//小黄块
		var $maskTop = $('#maskTop');//hover事件发生的容器范围
		var $largeImgContainer = $('#largeImgContainer');//大图的容器
		var $loading = $('#loading');//加载中图片
		var $largeImg = $('#largeImg');//大图
		var maskWidth = $mask.width();//黄块的宽
		var maskHeight = $mask.height();//黄块的高
		var maskTopWidth = $maskTop.width();//图片宽	
		var maskTopHeight = $maskTop.height();	//图片高
		$maskTop.hover(function() {
			//移入显示小黄块
			$mask.show();
			//动态加载对应的大图
			var src = $mediumImg.attr('src').replace('-m','-l');
			$largeImg.attr('src',src);
			//显示大图的容器
			$largeImgContainer.show();
			
			//大图加载完成的监听
			$largeImg.on('load',function(){
				//得到大图的尺寸
				var largeWidth = $largeImg.width();
				var largeHeight = $largeImg.height();
				//给大图容器设置尺寸
				$largeImgContainer.css({
					width:largeWidth/2,
					height:largeHeight/2,
				});
				//显示大图
				$largeImg.show();
				//隐藏加载进度条
				$loading.hide();
				$maskTop.mousemove(function(event) {
				//一定小黄块。移动大图
				//高频调用在鼠标移动的时候被反复调用
				//计算出小黄框的left和top
					var left = 0;
					var top = 0;
					// 事件的坐标 event 参数可以获取坐标 offsetX这个是事件发生元素的左上角的坐标 
					//clientX这个原点是窗口的左上角的坐标  pageX页面左上角的坐标
					var eventLeft = event.offsetX;
					var eventTop = event.offsetY;
					//给小黄快重新定位
					left = eventLeft - maskWidth/2;
					top = eventTop - maskHeight/2;
					if(left<0){
						left = 0;
					}else if(left > maskTopWidth-maskWidth){
						left = maskTopWidth-maskWidth;
					}
					if(top < 0){
						top = 0;
					}else if(top > maskTopHeight-maskHeight){
						top = maskTopHeight-maskHeight;
					}
					$mask.css({left:left,top:top});
					//移动大图
					//得到大图的坐标
					left = -left * largeWidth / maskTopWidth;
					top = -top * largeHeight / maskTopHeight;
					//设置大图的坐标
					$largeImg.css({left:left, top:top});
				});
			})
			
			
		}, function() {
			$mask.hide();
			// 隐藏大图容器
			$largeImgContainer.hide();
			//隐藏大图
			$largeImg.hide();

		});
	}

	//给li绑定hover事件当鼠标移入 选取到他的子标签，给他的子标签img添加样式，鼠标移入图片的时候上面大图也要跟随变化观察发现。li下面的img与上面大图img不同之处只有多了-m
	// 所以我们获得到li img的src 把它修改成大图，然后通过ID获取到大图的img。 再把属性src替换这样就可以显示对应的图片了
	function hoverMiniImg(){
		$('#icon_list>li').hover(function() {
			var $img = $(this).children();
			$img.addClass('hoveredThumb');
			var src = $img.attr('src').replace('.jpg','-m.jpg');
			$('#mediumImg').attr('src',src);
		}, function() {
			$(this).children().removeClass('hoveredThumb')
		});
	}




	function moveMiniImg(){
		//通过id获得下面所有的a标签
		var $as = $('#preview>h1>a');
		// 获得第一个a标签
		var $backward = $as.first();
		// 获得最后一个a标签
		var $forward = $as.last();
		// 获得ul
		var $ul = $('#icon_list');
		var SHOW_COUNT = 5;//一次能显示几个图片
		//通过ul选中所有的li。在通过length统计出li个总数
		var imgCount = $ul.children('li').length;//总图片数
		var moveCount = 0;//移动的次数（点右箭头的时候为正增加次数，点左箭头的时候为负减少次数）
		//锁边获得一个li获得他的宽度 为一次移动的距离
		var liWidth = $ul.children(':first').width();//每次移动的宽度



		//初始化的一个更新 attr 可以修改属性 attr可以修改值不是True或者false的
		


		//判读
		if(imgCount > SHOW_COUNT){
			// 把右标签设为可点击的样式
			$forward.attr('class','forward');
		}
		//给向右的按钮绑定点击属性
		$forward.click(function() {
			//更新向左的按钮
			//判断是否需要移动，如果不需要直接结束
			//这里的判断一旦满足就会return下面代码就会不执行
			if(moveCount === imgCount - SHOW_COUNT){
				return;
			}
			moveCount++;
			$backward.attr('class','backward');
			//更新向右的按钮
			if(moveCount === imgCount - SHOW_COUNT){
				$forward.attr('class','forward_disabled');
			}
			//移动
			$ul.css({
				left: -moveCount * liWidth
			});

		});
		//给左的按钮绑定点击属性
		$backward.click(function() {
			//更新向左的按钮
			//判断是否需要移动，如果不需要直接结束
			//这里的判断一旦满足就会return下面代码就会不执行
			if(moveCount === 0){
				return;
			}
			moveCount--;
			$forward.attr('class','forward');
			//更新向左的按钮
			if(moveCount === 0){
				$backward.attr('class','backward_disabled');
			}
			//移动
			$ul.css({
				left: -moveCount * liWidth
			});

		});
	}

	function clickProductTabs(){
		// 这里可以先获取在赋值给变量下面直接使用
		var $lis = $('#product_detail>ul>li');
		var $contents = $('#product_detail>div:gt(0)')

		$lis.click(function() {
			$(this).addClass('current').siblings().removeClass('current');

			var index = $(this).index();
			// 得到li的下标 上面获取到所有要显示的div第一个不是所以大于0 用$contents 的下标取出对应的div
			// 把它显示 div的兄弟有ul还有一个加入购物车的都不要所以是大于1的全部隐藏
			$contents.eq(index).show().siblings(':gt(1)').hide();
		});
	}


	// 获得ID 是minicart 的dib给他绑定hover事件鼠标移入显示他的子标签最后一个div给他显示出来，反之隐藏
	//点击时给自身添加样式minicart。反之一处这个样式
	function hoverminicart(){
		$('#minicart').hover(function(){
			$(this).addClass('minicart')
				.children(':last').show();
		},function(){
			$(this).removeClass('minicart')
				.children(':last').hide();
		})
	}





	// 这是一个选项卡操作，获得ul下面的所有li给他绑定点击事件 this是哪个？ 点击哪个li这个this就是谁，给当前this添加hover属性其余移出操作完成；
	function clickTabs(){
		$('#store_tabs > li').click(function(event) {
			$(this).addClass('hover').siblings().removeClass('hover');
		});
	}






	//给他绑定鼠标移入移出事件鼠标移入显示移出隐藏 下标大于0的 然后获得最后一个子标签
	//绑定点击事件如果点击最后一个标签下标大于0的隐藏
	function address(){
		var $select = $('#store_select');
		$select.hover(function() {
			$(this).children(':gt(0)').show();
		}, function() {
			$(this).children(':gt(0)').hide();
		})
		.children(':last')
		.click(function(event) {
			$select.children(':gt(0)').hide();
		});

	}

	function share(){
		var isOpen = false;//标识当前的状态 （初始化为关闭）
		// 在函数里面找没点击一次都会执行一遍里边的代码
		// 在外面只找一次就ok
		//修改qq空间显示不显示，西药修改4个标签，1是外层div宽度会发生变化，二是两个要显示出来的a标签要发生变化，show和hide之间切换
		//给傻帽绑定点击事件 ，傻帽下面的b标签有一个class属性有与没有这个样式，先获得了傻帽这个标签把它赋值给$shareMore这个变量
		//之后就可以用这个变量找到他的父元素div 以及使用prevAll方法找到两个a标签 注意他的标签下标是从傻帽开始为0向上的！！！！！！！！！！！！！！！！！！！！！！
		var $shareMore = $('#shareMore');
		var $parent = $shareMore.parent();
		var $as = $shareMore.prevAll('a:lt(2)');
		var $b = $shareMore.children(); 
		$('#shareMore').click(function(event) {
			if(isOpen){ //如果为True的话
				//打开状态，去关闭
				$parent.css('width',155);
				$as.hide();
				$b.removeClass('backword');
			}else{
				//关闭状态，去打开
				$parent.css('width',200);
				$as.show();
				$b.addClass('backword');
			}
			isOpen = !isOpen;
		});
	}


	//首先解释一下这个搜索框是写死的一个搜索框，search_helper 这个id对应的div是搜索框输入文本后显示的东西，
	//我们首先要把输入框的文本去除首位空格用的是trim 然后将内容赋值给前边的txt。进行判断if txt 存在有值的情况下就
	// 显示出要显示的内容就好了
	function seach(){
		$('#txtSearch').on('keyup focus',function(){
			//如果输入框有文本才显示列表
			var txt = $.trim(this.value);//trim 	可以去除首尾空格
			if (txt){
				$('#search_helper').show();
			}
		})
		.blur(function(event) {
			$('#search_helper').hide();
		});
	}




	//鼠标移入子菜单
	//总结：这个jquery 就是先获得了他们上面有ID的父级元素 通过这个id找到下面的div div中包含了h3菜单以及div二级菜单，我们找到
	//div后，获得当前的子标签的最后一个标签也就是使用：last来获取最后一个获取到之后。只要操作show 和dide 就ok了，
	//也就是移入显示移出隐藏！！！！！！！！！！！！！！！！！！！！！！！！！！！！
	function hoverSubMenu(){
		$('#category_items>div').hover(function() {
			$(this).children(':last').show();
		}, function() {
			$(this).children(':last').hide();
		});
	}





	// 总结 这个jquery其实就是等待页面元素加载完成之后，操作li属性为name=“show_hede”的属性，给他绑定什么时间呢？ 这个肯定是hover
	// 事件 还有一个重点是什么呢 他是选取多个不可直接选取li下面的标签进行show hide 操作            需要选取li标签观察下面要操作的
	// 属性 发现可以拼接，  那么我门拼接之后，进行show hide操作 那么万事大吉一切顺利！！！！！！！！
	// 移入显示移出隐藏
	// 给li绑定监听
	//
	function showhide(){
		$('[name=show_hide]').hover(function() {
			//显示
			// alert($(this.id))
			var id = this.id + "_items";
			$('#'+id).show();
		}, function() {
			//隐藏
			var id = this.id + "_items"
			$('#'+id).hide(); 
		});
	}
})


// 死记这句话对什么元素绑定什么监听进行什么dom操作 灵魂！！！！！！！！！！！！！！！！！！！！































