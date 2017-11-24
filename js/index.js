(function() {
  var $ = document.querySelector.bind(document),
      $$ = document.querySelectorAll.bind(document),
      $id = document.getElementById.bind(document),
      activeTagName = null,
      $tags = $$('#tags > .tag'),
      $projectsParent = $id('projects'),
      $projects = $$('#projects > .project'),
      $projectTags = $$('#projects .project-tag');

  // TAG SELECTION

  function getTagName($tag) {
    return $tag.classList[1];
  }

  function deactivateTag(tagName) {
    var tagSelector = '#tags > .tag.' + tagName;
    $(tagSelector).classList.remove('active');
    var projectSelector = '.project.' + tagName;
    $$(projectSelector).forEach(function($project) {
      $project.classList.remove('active');
    });
    var projectTagSelector = '.project-tag.' + tagName;
    $$(projectTagSelector).forEach(function($projectTag) {
      $projectTag.classList.remove('active');
    });
  }

  function activateTag(tagName) {
    var tagSelector = '#tags > .tag.' + tagName;
    $(tagSelector).classList.add('active');
    var projectSelector = '.project.' + tagName;
    $$(projectSelector).forEach(function($project) {
      $project.classList.add('active');
    });
    var projectTagSelector = '.project-tag.' + tagName;
    $$(projectTagSelector).forEach(function($projectTag) {
      $projectTag.classList.add('active');
    });
  }

  function clearActiveTagName() {
    deactivateTag(activeTagName);
    activeTagName = null;
  }

  function setActiveTagName(tagName) {
    if (activeTagName !== null) {
      deactivateTag(activeTagName);
    }
    activeTagName = tagName;
    activateTag(activeTagName);
  }

  function attachTagListener($tag) {
    var tagName = getTagName($tag);
    $tag.addEventListener('click', function() {
      if (tagName === activeTagName) {
        clearActiveTagName();
      } else {
        setActiveTagName(tagName);
      }
    }, false);
  }

  $tags.forEach(attachTagListener);
  $projectTags.forEach(attachTagListener);

  window.addEventListener('load', function() {
    $id('haiku').classList.remove('hide');
  })
})();
