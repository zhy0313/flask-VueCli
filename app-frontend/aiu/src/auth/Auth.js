/**
 * Created by farisi on 13.03.2017.
 */

class Auth{

  isAuhthendicated(){
    if(window.localStorage.getItem('is_authendicated')){
      return true;
    }
    return false;
  }

  setAuthendicated(access_token){
      window.localStorage.clear();
      window.localStorage.setItem("access_token", access_token);
      window.localStorage.setItem('is_authendicated', true);

  }

  destroyAuthendication(){
    window.localStorage.clear();
  }

  getAccessToken(){
    if (window.localStorage.getItem('is_authendicated')){
      return window.localStorage.getItem('access_token');
    }
    return null;
  }
}

export const auth = new Auth();
