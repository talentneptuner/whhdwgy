var g_class;
var show_desc = true
var show_course = false
var show_image = false
var show_prize = false
var desc_class = 'nav-item-active'
var image_calss = 'nav-item'
var prize_class = 'nav-item'
var course_class = 'nav-item'
var imgurl = ''
// pages/class/class.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
  
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var id = options.id
    wx.request({
      url: 'http://localhost:8000/getclassinfo/'+id,
      method: 'GET',
      header: {
        'content-type': 'application/json'
      },
      success: function(res){
        g_class = res.data
        that.setData({
          info:res.data,
          show_desc: show_desc,
          show_image:show_image,
          show_course:show_course,
          show_prize:show_prize,
          desc_class:desc_class,
          course_class:course_class,
          image_class:image_calss,
          prize_class:prize_class
        });
        wx.setNavigationBarTitle({
          title: res.data.name,
        })
      }
    })
  },

  showdesc:function(){
    var that = this;
    show_desc = true;
    show_image = false;
    show_course = false;
    show_prize = false;
    desc_class = 'nav-item-active'
    image_calss = 'nav-item'
    prize_class = 'nav-item'
    course_class = 'nav-item'
    that.setData({
      show_desc: show_desc,
      show_image: show_image,
      show_course: show_course,
      show_prize: show_prize,
      desc_class: desc_class,
      course_class: course_class,
      image_class: image_calss,
      prize_class: prize_class
    })
  },

  showimage:function(){
    var that = this;
    show_desc = false;
    show_image = true;
    show_course = false;
    show_prize = false;
    desc_class = 'nav-item'
    image_calss = 'nav-item-active'
    prize_class = 'nav-item'
    course_class = 'nav-item'
    that.setData({
      show_desc: show_desc,
      show_image: show_image,
      show_course: show_course,
      show_prize: show_prize,
      desc_class: desc_class,
      course_class: course_class,
      image_class: image_calss,
      prize_class: prize_class
    })
  },

  showcourse:function(){
    var that = this;
    show_desc = false;
    show_image = false;
    show_course = true;
    show_prize = false;
    desc_class = 'nav-item'
    image_calss = 'nav-item'
    prize_class = 'nav-item'
    course_class = 'nav-item-active'
    that.setData({
      show_desc: show_desc,
      show_image: show_image,
      show_course: show_course,
      show_prize: show_prize,
      desc_class: desc_class,
      course_class: course_class,
      image_class: image_calss,
      prize_class: prize_class
    })
  },

  showprize:function(){
    var that = this;
    show_desc = false;
    show_image = false;
    show_course = false;
    show_prize = true;
    desc_class = 'nav-item'
    image_calss = 'nav-item'
    prize_class = 'nav-item-active'
    course_class = 'nav-item'
    that.setData({
      show_desc: show_desc,
      show_image: show_image,
      show_course: show_course,
      show_prize: show_prize,
      desc_class: desc_class,
      course_class: course_class,
      image_class: image_calss,
      prize_class: prize_class
    })
  },

  saveAction: function(res){
      var id = res.currentTarget.dataset.id
      // console.log(g_class.images)
      for (let i = 0 ;i< g_class.images.length;i++){
        if(g_class.images[i].id == id){
          imgurl = g_class.images[i].image
          break
        }
      }
      //console.log(imgurl)
      wx.showActionSheet({
        itemList: ['保存图片',],
        success : function(tap){
          if(tap.tapIndex === 0){
            wx.downloadFile({
              url:imgurl,
              success:function(res){
               // console.log(res)
                wx.saveImageToPhotosAlbum({
                  filePath: res.tempFilePath,
                  success:function(res){
                    wx.showToast({
                      title: '保存成功',
                    })
                  },
                  fail:function(res){
                    wx.showToast({
                      title: '保存失败',
                    })
                  }
                })
              }
            })
          }
        }
      })
  },

  previewImages:function(res){
    var id = res.currentTarget.dataset.id
    // console.log(g_class.images)
    for (let i = 0; i < g_class.images.length; i++) {
      if (g_class.images[i].id == id) {
        imgurl = g_class.images[i].image
        break
      }
    }
    wx.previewImage({
      urls: [imgurl,],
    })
  }

 
})